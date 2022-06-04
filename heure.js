let elHeure = document.getElementById("heure");
window.setInterval(() => {
  {
    elHeure.innerHTML = new Date();
  }
}, 1000);
