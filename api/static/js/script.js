setTimeout(function () {
    var element = document.createElement("div");
    element.style.backgroundColor = "white";
    element.innerHTML = 'Preparando Testes... <br> Para acessar a Pagina Principal <a href="http://192.168.0.50:3000">React Page!</a>';
    document.body.appendChild(element);
  }, 5000);



  const ratings = document.getElementsByName('rating');
  let ratingValue;

  for (let i = 0; i < ratings.length; i++) {
      ratings[i].addEventListener('change', function () {
          ratingValue = this.value;
          calculateAverage();
      });
  }

  function calculateAverage() {
      let total = 0;
      for (let i = 0; i < ratings.length; i++) {
          if (ratings[i].checked) {
              total += parseInt(ratings[i].value);
          }
      }
      const average = total / ratings.length;
      document.getElementById('average-rating').innerHTML = `Aprovação: ${average.toFixed(1)}`;
  }
