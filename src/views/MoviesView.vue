<template>
    <div class="header">
        <h1>Movies</h1>
    </div>
    <div class="container mt-4">
        <div class="row g-4">
            <div class ="col-md-6 mb-3" v-for="movie in movies" :key="movie.id">
                <div class="card h-100 d-flex flex-row">
                    <img :src="movie.poster" class="img-fluid rounded-start" alt="Movie Poster" style=" object-fit:cover; width:160px; height: auto;"/>
                    <div class="card-body">
                        <h5 class="card-title" style:="white-space: normal; word-wrap: break-word;">{{ movie.title }}</h5>
                        <p class="card-text" style:="white-space: normal;">{{movie.description}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>
import { ref, onMounted} from "vue";

onMounted(() => {
    fetchMovies()
})

let movies = ref([]);

function fetchMovies(){
    fetch('/api/v1/movies',{
    })
    .then(response => response.json())
    .then(data=>{
        console.log(data)
        movies.value = data
    })
    .catch(error=> console.log(eror))
}

</script>


<style scoped>
.header{
    margin: 15px;
    padding: 20px;
}

.card{
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 20x 8px rgba(0, 0, 0, 0.1);
}

.card-img-top{
    height: 100px;
    object-fit:cover;
}

.movie-poster{
    width:100%;
    height:auto;
    border-radius:8px;
}

.movie-title{
    font-size:1.25rem;
    margin-top:0.5rem;
}

.movie-description{
    font-size:0.9rem;
    color:dimgray;
    
}
</style>