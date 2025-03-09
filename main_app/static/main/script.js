document.addEventListener("DOMContentLoaded", () => {
    // ✅ GSAP: Page Load Animations
    gsap.from("h1", { opacity: 0, y: -50, duration: 1 });
    gsap.from("p", { opacity: 0, y: 30, duration: 1, delay: 0.5 });
    gsap.from("button", { opacity: 0, scale: 0.8, duration: 1, delay: 1 });

    // ✅ GSAP: Section Fade-in on Scroll
    gsap.utils.toArray("section").forEach(section => {
        gsap.from(section, {
            opacity: 0,
            y: 50,
            duration: 1,
            scrollTrigger: {
                trigger: section,
                start: "top 80%",
                toggleActions: "play none none none"
            }
        });
    });

    // ✅ Parallax Scrolling Effect
    gsap.to(".parallax", {
        scrollTrigger: {
            trigger: ".parallax",
            start: "top bottom",
            end: "bottom top",
            scrub: true,
        },
        y: -100
    });

    // ✅ Auto-hide Flash Messages (Bootstrap alerts)
    setTimeout(() => {
        let alerts = document.querySelectorAll(".alert");
        alerts.forEach(alert => {
            gsap.to(alert, { opacity: 0, duration: 1, onComplete: () => alert.remove() });
        });
    }, 4000); // Hides after 4 seconds

    // ✅ Smooth Scrolling to Sections
    document.querySelectorAll("a[href^='#']").forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            e.preventDefault();
            let target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // ✅ Dark Mode Toggle
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    if (darkModeToggle) {
        darkModeToggle.addEventListener("click", () => {
            document.body.classList.toggle("dark-mode");
            localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
        });

        // Apply dark mode if it was previously enabled
        if (localStorage.getItem("darkMode") === "true") {
            document.body.classList.add("dark-mode");
        }
    }
});
