<template>
    <div class="add-movie-form-view mt-4">
      <h1>Upload</h1>
      <MovieForm />
    </div>
</template>
  
<script setup>
  import MovieForm from '@/components/MovieForm.vue';
</script>

<style scoped>
.add-movie-form-view{
  padding: 20px;

}

h1{
  color:cornflowerblue;
  margin: 10px 40px 10px 40px;
}



</style>