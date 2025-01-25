gsap.from("#mask-stroke", {
  drawSVG: "0%",
  scrollTrigger: {
    trigger: "#page",
    start: "-7% top",
    end: "bottom+=20% bottom",
    scrub: 1
  }
});

gsap.from("#stroke", {
  "--dashOffset": 1000,
  delay: 1,
  scrollTrigger: {
    trigger: "#page",
    start: "-5% top",
    end: "bottom+=20% bottom",
    scrub: 1
  }
});

let text = gsap.utils.toArray(".revealer-inner");
text.forEach((el, i) => {
  gsap.from(el, {
    yPercent: 120,
    duration: 1,
    delay: el.classList.contains("page-title-secondary") ? 2 : 1,
    scrollTrigger: {
      trigger: el,
      start: "top center",
      end: "bottom top",
      toggleActions: "restart pause resume reset"
    }
  });
});

let images = gsap.utils.toArray(".revealer-img");
images.forEach((el) => {
  gsap.from(el, {
    opacity: 0,
    yPercent: 10,
    scale: 1.2,
    duration: 2,
    scrollTrigger: {
      trigger: el,
      start: "top bottom",
      end: "bottom top",
      toggleActions: "restart pause resume pause"
    }
  });
});
