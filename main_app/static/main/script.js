document.addEventListener("DOMContentLoaded", () => {
    gsap.from("header h1", { opacity: 0, y: -50, duration: 1 });
    gsap.from("header p", { opacity: 0, y: 50, duration: 1, delay: 0.5 });
    gsap.from("header button", { opacity: 0, scale: 0.5, duration: 1, delay: 1 });

    gsap.from("#about-section h2", { opacity: 0, x: -100, duration: 1, scrollTrigger: "#about-section" });
    gsap.from("#about-section p", { opacity: 0, x: 100, duration: 1, scrollTrigger: "#about-section" });

    gsap.from("#signup-section h2", { opacity: 0, y: 50, duration: 1, scrollTrigger: "#signup-section" });
});

function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({ behavior: "smooth" });
}
