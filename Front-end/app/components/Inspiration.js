import React from "react";

const Inspiration = () => {
  return (
    <section className="py-16">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-4 gap-8">
          <div className="col-span-1">
            <img
              src="https://assets-global.website-files.com/617825a38a48f37525a3c16f/62d8176e6385fd2237826d53_animation.svg"
              alt="Image 1"
              className="rounded-lg"
            />
            <p className="mt-4">3D</p>
          </div>
          <div className="col-span-1">
            <img
              src="https://assets-global.website-files.com/617825a38a48f37525a3c16f/62d81784f14973fe80bd8d29_audio.svg"
              alt="Image 2"
              className="rounded-lg"
            />
            <p className="mt-4">Podcast</p>
          </div>
          <div className="col-span-1">
            <img
              src="https://assets-global.website-files.com/617825a38a48f37525a3c16f/62d8176517f57ff51da79087_design.svg"
              alt="Image 3"
              className="rounded-lg"
            />
            <p className="mt-4">Design</p>
          </div>
          <div className="col-span-1">
            <img
              src="https://assets-global.website-files.com/617825a38a48f37525a3c16f/62d8170ea559e045188de682_education.svg"
              alt="Image 4"
              className="rounded-lg"
            />
            <p className="mt-4">Education</p>
          </div>
        </div>
        <div className="grid grid-cols-4 gap-8">
          <div className="col-span-1">
            <img
              src="https://assets-global.website-files.com/617825a38a48f37525a3c16f/62d8170506f22b24b1617fe1_fitness.svg"
              alt="Image 1"
              className="rounded-lg"
            />
            <p className="mt-4">Fitness</p>
          </div>
          <div className="col-span-1">
            <img
              src="https://assets-global.website-files.com/617825a38a48f37525a3c16f/62d815009ec3bf46d30f09bb_software.svg"
              alt="Image 2"
              className="rounded-lg"
            />
            <p className="mt-4">Software dev</p>
          </div>
          <div className="col-span-1">
            <img
              src="https://assets-global.website-files.com/617825a38a48f37525a3c16f/62d81543cb2b3b104c356ba4_photography.svg"
              alt="Image 3"
              className="rounded-lg"
            />
            <p className="mt-4">Photography</p>
          </div>
          <div className="col-span-1">
            <img
              src="https://assets-global.website-files.com/617825a38a48f37525a3c16f/62d814f917f57f7f76a772ba_writing.svg"
              alt="Image 4"
              className="rounded-lg"
            />
            <p className="mt-4">Blog</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Inspiration;
