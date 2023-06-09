// 404 page
import React from "react";
import Link from "next/link";

const NotFoundPage = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white">
      <h1 className="text-6xl font-bold mb-4">404</h1>
      <p className="text-2xl mb-8">Page not found</p>
      <Link href="/">
        <a className="text-blue-500 hover:underline">Go back to Home</a>
      </Link>
    </div>
  );
};

export default NotFoundPage;
