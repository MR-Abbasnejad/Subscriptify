import React from "react";

const Navbar = () => {
  return (
    <nav className="flex items-center justify-between bg-white p-4">
      <div className="text-blue-600 font-bold text-lg">Subscriptify</div>
      <div className="flex items-center">
        <input
          type="text"
          placeholder="Search"
          className="bg-blue-100 text-white px-4 py-2 rounded-md mr-4"
        />
        <button className=" bg-white  border border-blue-500 text-blue-500 px-4 py-2 rounded-md">
          Connect Wallet
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
