const items = document.querySelectorAll('.panel-item');
  items.forEach(item => {
    item.addEventListener('click', function() {
      const currentActive = document.querySelector('.panel-item.active');
      if (currentActive) {
        currentActive.classList.remove('active');
      }
      this.classList.add('active');
    });
  });

function confirmDelete(){
if(confirm("Do you want to delete")){
alert("Deleted");
}
else{
alert("Cancelled");
}
}