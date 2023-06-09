// Home Page

import Hero1 from "./components/Hero1";
import HeroSection from "./components/HeroSection";
import Navbar from "./components/Navbar";
import Inspiration from "./components/Inspiration";
import LiteBox from "./components/LiteBox";
import Footer from "./components/Footer";

export default function Home() {
  return (
    <main>
      <Navbar />

      <HeroSection />

      <Hero1 />
      <Inspiration />
      <LiteBox />
      <Footer />
    </main>
  );
}
