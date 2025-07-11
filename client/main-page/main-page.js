document.getElementById('search-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const searchTerm = document.getElementById('search-input').value.toLowerCase();
  const elements = document.querySelectorAll('slot');
  for (let i = 0; i < elements.length; i++) {
    const element = elements[i];
    const text = element.textContent.toLowerCase();
    if (text.includes(searchTerm)) {
      element.style.display = 'grid';
    } else {
      element.style.display = 'none';
    }
  }
});