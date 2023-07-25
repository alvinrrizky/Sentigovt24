document.addEventListener('alpine:init', () => {
    Alpine.store('accordion', {
        tab: 0
    });
    Alpine.data('accordion', (idx) => ({
        init() {
            this.idx = idx;
        },
        idx: -1,
        handleClick() {
            this.$store.accordion.tab = this.$store.accordion.tab === this.idx ? 0 : this.idx;
        },
        handleRotate() {
            return this.$store.accordion.tab === this.idx ? 'rotate-180' : '';
        },
        handleToggle() {
            return this.$store.accordion.tab === this.idx ? `max-height: ${this.$refs.tab.scrollHeight}px` : '';
        }
    }));
})

function togglePopup1() {
    document.getElementById("popupId-1").classList.toggle("active");
}

function togglePopup2() {
    document.getElementById("popupId-2").classList.toggle("active");
}

function togglePopup3() {
    document.getElementById("popupId-3").classList.toggle("active");
}

window.onload = function () {
    const toTop = document.querySelector(".to-top");

    window.addEventListener("scroll", function () {
        if (window.pageYOffset > 100) {
            toTop.classList.add("active");
        } else {
            toTop.classList.remove("active");
        }
    });
};

// typing text animation script
var typed = new Typed(".typing", {
    strings: ["See Beyond the Noise in <br/> The 2024 Race", "Your voice is yours,<br/> use it wisely", "Together we can change<br/> the future"],
    typeSpeed: 100,
    backSpeed: 60,
    loop: true
});
