import React from "react";

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white py-8">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center justify-center">
          <nav className="flex flex-wrap justify-center sm:justify-start">
            <a
              href="#"
              className="text-gray-300 hover:text-white px-4 py-2 block"
            >
              About Us
            </a>
            <a
              href="#"
              className="text-gray-300 hover:text-white px-4 py-2 block"
            >
              GitHub
            </a>
            <a
              href="#"
              className="text-gray-300 hover:text-white px-4 py-2 block"
            >
              Twitter
            </a>
            <a
              href="#"
              className="text-gray-300 hover:text-white px-4 py-2 block"
            >
              Contact Us
            </a>
          </nav>
        </div>
        <div className="text-center mt-4">
          <p className="text-gray-300">
            &copy; 2023. gic.io. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
