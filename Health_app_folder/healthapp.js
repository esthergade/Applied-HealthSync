const button_report = document.getElementById("button");

button_report.addEventListener("click", function() {
    const bloodPressure = prompt("Please enter your blood pressure:");
    console.log(bloodPressure);

    const currentDate = new Date();
    console.log(currentDate);

    const data = {
      bloodPressure: bloodPressure,
      currentDate: currentDate,
    };

});

function showImage(image_path) {
  document.getElementById('image')
                    .style.display = "block"
  document.getElementById("Show_Image")
                    .style.display = "none";
}
