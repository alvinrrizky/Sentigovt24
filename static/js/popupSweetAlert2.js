// document.getElementById("editBacapres").addEventListener("submit", function(event) {
//     event.preventDefault(); // Prevent the form from submitting normally
//     var myButton = document.getElementById("saveEditBacapres");
//     var id = myButton.getAttribute("data-id");
//     // Perform the form submission using AJAX or fetch
//     // Replace the URL and other parameters with your actual values
//     fetch(`/bacapres/edit/${id}`, {
//       method: "POST",
//       body: new FormData(event.target) // Use FormData to get form data
//     })
//     .then(response => {
//       if (response.ok) {
//         // Form submission was successful, show success popup
//         Swal.fire({
//             icon: 'success',
//             title: 'Bacapres has been added',
//             showConfirmButton: false,
//             timer: 1500
//         });
//         setTimeout(function() {
//             // Reload the current page
//             window.location.href = '/bacapres';
//           }, 2000);
//       } else {
//         // Form submission failed, show error popup
//         Swal.fire({
//             icon: 'error',
//             title: 'Bacapres creation failed',
//             showConfirmButton: false,
//             timer: 3000
//         });
//       }
//     })
//     .catch(error => {
//       // Handle any error that occurred during form submission
//       console.error("Error:", error);
//       Swal.fire({
//         title: "Error",
//         text: "An error occurred during form submission",
//         icon: "error"
//       });
//     });
//   });


document.addEventListener('DOMContentLoaded', function () {
  var myButton = document.getElementById('deleteAllBacapres');

  myButton.addEventListener('click', function () {
    Swal.fire({
      title: "Are you sure?",
      text: "You won't be able to revert this!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: "Yes, delete All!",
    }).then((result) => {
      if (result.isConfirmed) {
        const url = `/sentiment/history/delete/all/`;
        $.ajax({
          url: url,
          type: "POST",
          headers: {
            "X-CSRFToken": getCookie("csrftoken")
          },
          success: function (response) {
            Swal.fire('Deleted!', 'Your data has been deleted.', 'success');
            location.reload()
            // Lakukan tindakan tambahan setelah penghapusan data berhasil
          },
          error: function (xhr, status, error) {
            Swal.fire('Error!', 'An error occurred while deleting the data.', 'error');
            // Lakukan tindakan tambahan jika terjadi kesalahan saat menghapus data
          }
        });
      }
    });
  });
});

// Add an event listener to the form submit event
document.getElementById("createBacapres").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the form from submitting normally

  // Perform the form submission using AJAX or fetch
  // Replace the URL and other parameters with your actual values
  fetch("/bacapres/create", {
      method: "POST",
      body: new FormData(event.target) // Use FormData to get form data
    })
    .then(function (response) {
      if (response.status === 400) {
        return response.json();
      } else {
        // Form submission was successful, show success popup
        Swal.fire({
          icon: 'success',
          title: 'Bacapres has been added',
          showConfirmButton: false,
          timer: 1500
        });
        setTimeout(function () {
          // Reload the current page
          window.location.href = '/bacapres';
        }, 2000);
      }
    })
    .then(function (errors) {
      console.log(errors)
      document.getElementById("name_err").innerText = ""
      document.getElementById("keyword_err").innerText = ""
      document.getElementById("avatar_err").innerText = ""

      if (errors.hasOwnProperty('name')) {
        document.getElementById("name_err").innerText = errors.name[0].message
      }
      if (errors.hasOwnProperty('keyword')) {
        document.getElementById("keyword_err").innerText = errors.keyword[0].message
      }
      if (errors.hasOwnProperty('avatar')) {
        document.getElementById("avatar_err").innerText = errors.avatar[0].message
      }
      // Form submission failed, show error popup
      Swal.fire({
        icon: 'error',
        title: 'Bacapres creation failed',
        showConfirmButton: false,
        timer: 3000
      });
    })
    .catch(function (errors) {})
});

// Helper function to get the value of a cookie
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Check if the cookie name matches the given name
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}