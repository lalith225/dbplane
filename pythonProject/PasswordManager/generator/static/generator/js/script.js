function copyPassword() {
    const input = document.getElementById("generatedPassword");
    if (!input) return;
    input.focus();
    input.select();
    input.setSelectionRange(0, 99999);
    document.execCommand("copy");
    window.getSelection().removeAllRanges();
    input.blur();
    const msg = document.getElementById("copyMsg");
    if (msg) {
        msg.classList.add("show");
        setTimeout(() => msg.classList.remove("show"), 1200);
    }
}
