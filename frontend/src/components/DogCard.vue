<template>
  <div class="card">
  <div class="card-image">
    <figure class="image is-4by3">
      <img :src="image_url" loading="lazy">
    </figure>
  </div>
  <div class="card-content">
    <div class="media">
      <div class="media-content">
        <p class="title is-4">{{name}}</p>
        <p class="tag is-link">{{breed}}</p>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
  import { defineProps } from 'vue'

  // expects props options
  const props = defineProps({
    name: String,
    image_url: String,
    breed: String
  })
  
</script>

<style>

</style>