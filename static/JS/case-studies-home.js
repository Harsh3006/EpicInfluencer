var case_content = document.getElementsByClassName('case-content');
if (case_content) {
  var product_type = 'all', industry_type = 'all';
  filterProduct(product_type);
  filterIndustry(industry_type);

  function filterProduct(type) {
    product_type = type;
    filterCases(product_type, industry_type);
  }
  function filterIndustry(type) {
    industry_type = type;
    filterCases(product_type, industry_type);
  }
  function filterCases(type1, type2) {
    for (let i = 0; i < case_content.length; i++) {
      if ((case_content[i].classList.contains(type1)) && (case_content[i].classList.contains(type2))) {
        case_content[i].classList.add('show');
      }
      else {
        case_content[i].classList.remove('show');
      }
    }
  }
  // Add active class to the current control button (highlight it)
  var product_ul = document.getElementById("product_types");
  var industry_ul = document.getElementById("industry_types");
  var product_btns = product_ul.getElementsByClassName("product_btn");
  var industry_btns = industry_ul.getElementsByClassName("industry_btn");
  for (let i = 0; i < product_btns.length; i++) {
    product_btns[i].addEventListener("click", function () {
      var current_product = product_ul.getElementsByClassName("active");
      current_product[0].className = current_product[0].className.replace(" active", "");
      this.className += " active";
    });
  }
  for (var i = 0; i < industry_btns.length; i++) {
    industry_btns[i].addEventListener("click", function () {
      var current_industry = industry_ul.getElementsByClassName("active");
      current_industry[0].className = current_industry[0].className.replace(" active", "");
      this.className += " active";
    });
  }
}
