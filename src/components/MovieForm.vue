<template>
  <!-- Form -->
  <form method="POST" enctype="multipart/form-data" @submit.prevent="saveMovie" id="movieForm">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title:</label>
      <input type="text" id="title" name="title" class="form-control" v-model="title">
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description:</label>
      <textarea id="description" name="description" class="form-control" v-model="description"></textarea>
    </div>

    <!--error/success message-->
    <div v-if="successMessage" class="alert alert-success" id="success">{{ successMessage }}</div>
    <div v-if="errorMessage.length > 0" class="alert alert-danger" id="error">
      <ul>
        <li v-for="(message, index) in errorMessage" :key="index">{{ message }}</li>
      </ul>
    </div> 
    
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster:</label>
      <input type="file" id="poster" name="poster" class="form-control" @change="handleFileChange">
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let csrf_token = ref('');
let successMessage = ref('');
let errorMessage = ref([]);

let title = ref('');
let description = ref('');
let poster = ref(null);

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
    .catch(error => {
      console.error('Error fetching CSRF token:', error);
    });
}

onMounted(() => {
  getCsrfToken();
});

function handleFileChange(event) {
  poster.value = event.target.files[0];
}

function saveMovie() 
{

let movieForm = document.getElementById('movieForm');
let form_data = new FormData();

form_data.append('title', title.value);
form_data.append('description', description.value);
form_data.append('poster', poster.value);

    try {
        fetch('/api/v1/movies',{
            method: 'POST',
            headers: {
                //'Content-Type': 'application/json',
                'X-CSRFTOKEN' : csrf_token.value
            },
            body: form_data
        })
        .then(response => response.json())
        .then(data =>{
            console.log("Success:", data);

            movieForm.reset();

        })
        .catch(function(error){
          console.error('Could not fetch operation:', error)

          successMessage.value =[];
          errorMessage.value= '';

          if(!formData.value.title.trim() || !formData.value.description.trim() || !formData.poster){
            errorMessage.value.push("Error: All fields are required.");
          }

        })

      
        /*const data = res.json().catch(() =>({}))
        if (!res.ok||!data.access_token) {
            throw new Error(data.error || 'Login failed')
        }*/
    }
    catch (e) {
        console.error(e.message);
    }
}

</script>

<style scoped>
#movieForm{
  margin: 10px 40px 10px 40px;
}

#success{
  padding: 10px;
  background-color: #7bdb91;
  border-radius: 8px;
  color: white;
  font-size: 10px;
}
#error{
  padding: 10px;
  background-color:crimson;
  border-radius: 8px;
  color: white;
  font-size: 10px;
}

</style>