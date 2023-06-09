import React from "react";

const HeroSection = () => {
  return (
    <section className="flex items-center justify-center bg-gray-100 py-16">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center">
          <div className="md:w-1/2">
            <h1 className="text-4xl text-black font-bold mb-4">
              Unlock the full potential of your content with our revolutionary
              new monetization platform.
            </h1>
            <br />

            <p className="text-lg text-gray-700 mb-8">
              with us anyone can earn their first dollar online . Just start
              with what you know we are here for supporting you
            </p>
            <br />
            <button className="bg-white text-blue-500 px-4 py-2 rounded-md border border-blue-500">
              Kick start your journey
            </button>
          </div>
          <div className="md:w-1/2">
            <img
              src="https://substackcdn.com/image/fetch/w_1166,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Fhome_page%2Fhero_image.png"
              alt="Hero Image"
              className="rounded-lg"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
