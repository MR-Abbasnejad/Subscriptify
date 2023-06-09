import React from "react";

const Hero1 = () => {
  return (
    <div>
      <section className="flex items-center justify-between bg-gray-100 py-16">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row items-center">
            <div className="md:w-2/3">
              <h1 className="text-4xl text-black font-bold mb-4">
                Make your own road
              </h1>
              <p className="text-lg text-gray-700 mb-8">
                You don't have to be a tech expert or even understand how to
                start a business. You just gotta take what you know and sell it.
              </p>
            </div>
            <div className="md:w-1/3">
              <img
                src="https://substackcdn.com/image/fetch/w_1136,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Fhome_page%2Fbenefit-3.png"
                alt="Hero Image"
                className="rounded-lg w-full"
              />
            </div>
          </div>
        </div>
      </section>

      <section className="flex items-center justify-between bg-gray-100 py-16">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row items-center">
            <div className="md:w-1/3">
              <img
                src="https://substackcdn.com/image/fetch/w_1136,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Fhome_page%2Fbenefit-3.png"
                alt="Hero Image"
                className="rounded-lg w-full"
              />
            </div>
            <div className="md:w-2/3 pr-8">
              {" "}
              {/* Added pr-8 for right padding */}
              <h1 className="text-4xl text-black font-bold mb-4">
                Sell anywhere, anytime using cryptocurrency
              </h1>
              <p className="text-lg text-gray-700 mb-8">
                Empower your customers to shop with ease, no matter where they
                are or when they want to buy. Our platform allows you to accept
                payments using the latest in cryptocurrency technology, making
                transactions fast, secure, and hassle-free.
              </p>
            </div>
          </div>
        </div>
      </section>
      <section className="flex items-center justify-between bg-gray-100 py-16">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row items-center">
            <div className="md:w-2/3">
              <h1 className="text-4xl text-black font-bold mb-4">
                You make it, you own it.
              </h1>
              <p className="text-lg text-gray-700 mb-8">
                You always own your intellectual property, mailing list, and
                subscriber payments. With full editorial control and no
                gatekeepers, you can do the work you most believe in.
              </p>
            </div>
            <div className="md:w-1/3">
              <img
                src="https://substackcdn.com/image/fetch/w_1136,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Fhome_page%2Fbenefit-1.png"
                alt="Hero Image"
                className="rounded-lg w-full"
              />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Hero1;
