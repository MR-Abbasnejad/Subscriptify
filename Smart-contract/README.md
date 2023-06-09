# NFT Subscription Contract
The NFT Subscription contract is a smart contract built on the Ethereum blockchain that enables creators to share exclusive content with subscribers through NFTs (Non-Fungible Tokens).

## Features
Creating NFTs with Exclusive Content: Creators can create NFTs that contain exclusive content and set a subscription price for accessing that content.

Buying Subscriptions: Users can purchase subscriptions to access the exclusive content shared by creators. The payment is directly transferred to the creator.

Subscription Expiry: Subscriptions have an expiry date, after which the subscriber no longer has access to the exclusive content.

NFT Gating: NFTs are used to gate access to exclusive content. Only subscribers who hold the specific NFT associated with a subscription can access the content.

Platform Fee: A platform fee of 3% is deducted from the subscription price and transferred to the platform owner. The remaining amount is sent to the creator.

## How to Use
### For Creators
Deploy the Contract: Deploy the NFT Subscription contract on the Ethereum blockchain. Provide the platform owner address and the Chainlink Price Feed address during deployment.

Create NFTs: Use the createNFT function to create NFTs with exclusive content. Set the content URI and subscription price. The NFTs will be minted to your wallet.

### For Subscribers
Buy Subscriptions: Browse the available NFTs and select the content you want to access. Use the buySubscription function to purchase a subscription. Pay the subscription price, which will be transferred to the creator, and receive the associated NFT.

Access Exclusive Content: As a subscriber, if you own the NFT associated with a subscription, you can access the exclusive content through an NFT gated website or application.

Subscription Renewal: Subscriptions have an expiry date. To continue accessing the exclusive content, renew your subscription by purchasing another one before the expiry date.

## Security Considerations
Thoroughly test and audit the contract before deploying it to the mainnet. No contract can be guaranteed to be completely bug-free or secure.

Verify the contract address and transaction details before making any payments or transactions.

Seek assistance from a knowledgeable developer or auditor if you have any concerns or encounter issues.

setToken: allows the contract owner to update the address of the ERC20 token contract.

getSubscription: allows anyone to retrieve the details of a subscriber's subscription by providing the subscriber's address.
