// Active menu sidenav
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('.itemActive').forEach(link => {
    if (link.href.includes(`${activePage}`)) {
        link.classList.add('active');
    }
})

// Href
function goToDetailPage(url) {
    window.location.href = url;
}

function toggleMenuMobile() {
    document.getElementById("menuMobile").classList.toggle("activeMenuMobile");
    $('body').addClass('overflow-hidden');
}

function toggleRankingMobile() {
    document.getElementById("rankingMobile").classList.toggle("activeMenuMobile");
    $('body').addClass('overflow-hidden');
}

function closeModal() {
    $('body').removeClass('overflow-hidden');
}