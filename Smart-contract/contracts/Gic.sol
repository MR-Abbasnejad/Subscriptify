// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract NFTSubscription is ERC1155, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private subscriptionIds;
    Counters.Counter private nftIds;

    uint256 public constant DURATION = 30 days; // Expiry duration for subscriptions

    struct Subscription {
        uint256 id;
        address payable creator; // Wallet address of the creator
        address payable subscriber; // Wallet address of the subscriber
        uint256 expiryDate; // Expiry date of the subscription
        uint256 price; // Price paid for the subscription
        uint256[] nftIds; // NFT IDs associated with the subscription
    }

    struct NFT {
        uint256 id;
        uint256 subscriptionId;
        bool gated;
        string contentURI;
    }

    mapping(uint256 => Subscription) public subscriptions; // Mapping to store subscriptions
    mapping(uint256 => NFT) public nfts; // Mapping to store NFTs

    mapping(address => uint256[]) public userSubscriptions; // Mapping to track subscriptions per user

    address payable public platformOwner; // Address of the platform owner

    AggregatorV3Interface private priceFeed; // Chainlink Price Feed

    constructor(address payable _platformOwner, address _priceFeedAddress) ERC1155("") {
        platformOwner = _platformOwner;
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    // Function to create and gate an NFT with exclusive content
    function createNFT(string calldata contentURI, uint256 subscriptionPrice) external returns (uint256) {
        uint256 nftId = nftIds.current();
        nftIds.increment();

        nfts[nftId] = NFT(nftId, 0, true, contentURI);

        // Mint the NFT to the creator
        _mint(msg.sender, nftId, 1, "");

        // Emit an event for NFT creation
        emit NFTCreated(nftId, msg.sender, contentURI);

        // Create a subscription for the NFT
        uint256 subscriptionId = _createSubscription(msg.sender, subscriptionPrice);
        nfts[nftId].subscriptionId = subscriptionId;

        // Associate the NFT with the subscription
        subscriptions[subscriptionId].nftIds.push(nftId);

        // Return the NFT ID
        return nftId;
    }

    // Function to buy a subscription for a specific creator
    function buySubscription(uint256 subscriptionId) external payable {
    require(subscriptionId > 0 && subscriptionId <= subscriptionIds.current(), "Invalid subscription ID");

    Subscription storage subscription = subscriptions[subscriptionId];
    require(subscription.subscriber == address(0), "Subscription already purchased");
    require(msg.value >= subscription.price, "Insufficient funds");

    // Calculate the platform fee
    uint256 platformFee = subscription.price * 3 / 100;

    // Calculate the creator amount after deducting the platform fee
    uint256 creatorAmount = subscription.price - platformFee;

    // Transfer the platform fee to the platform owner
    platformOwner.transfer(platformFee);

    // Transfer the remaining amount to the creator
    subscription.creator.transfer(creatorAmount);

    // Transfer all associated NFTs to the subscriber
    uint256[] memory nftIdsArr = subscription.nftIds;
    for (uint256 i = 0; i < nftIdsArr.length; i++) {
        uint256 nftId = nftIdsArr[i];
        if (nfts[nftId].gated) {
            _safeTransferFrom(address(this), msg.sender, nftId, 1, "");
        }
    }

    // Emit an event for subscription purchase
    emit SubscriptionPurchased(subscriptionId, msg.sender, nftIdsArr, subscription.price);
}


    // Function to check if a subscription is expired
    function isSubscriptionExpired(uint256 subscriptionId) external view returns (bool) {
        require(subscriptionId > 0 && subscriptionId <= subscriptionIds.current(), "Invalid subscription ID");

        Subscription storage subscription = subscriptions[subscriptionId];
        return (subscription.expiryDate <= block.timestamp);
    }

    // Function to get the current time from the Chainlink Price Feed
    function _getCurrentTime() internal view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price");
        return uint256(price);
    }

    // Internal function to create a new subscription
    function _createSubscription(address creator, uint256 price) internal returns (uint256) {
        uint256 subscriptionId = subscriptionIds.current();
        subscriptionIds.increment();

        Subscription storage subscription = subscriptions[subscriptionId];
        subscription.id = subscriptionId;
        subscription.creator = payable(creator);
        subscription.subscriber = payable(address(0));
        subscription.expiryDate = 0;
        subscription.price = price;

        // Emit an event for subscription creation
        emit SubscriptionCreated(subscriptionId, creator, price);

        return subscriptionId;
    }

    // Event emitted when an NFT is created
    event NFTCreated(uint256 indexed nftId, address creator, string contentURI);

    // Event emitted when a subscription is purchased
    event SubscriptionPurchased(
        uint256 indexed subscriptionId,
        address subscriber,
        uint256[] nftIds,
        uint256 price
    );

    // Event emitted when a subscription is created
    event SubscriptionCreated(uint256 indexed subscriptionId, address creator, uint256 price);
}
