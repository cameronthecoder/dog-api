<template>
<div>
  <section class="hero is-link has-text-centered">
    <div class="hero-body">
      <p class="title is-1">
        Doggos
      </p>
      <p class="subtitle">
        An website with a bunch of cute dogs.
      </p>
    </div>
  </section>
  <section class="section has-background-light">
    <div class="container">
      <h3 class="title is-3">Add your furry friend:</h3>
      <form @submit.prevent="addDog">
        <div class="field">
          <label class="label">Name</label>
          <div class="control">
            <input class="input is-large" type="text" placeholder="Dog name" required v-model="name">
          </div>
        </div>


        <div class="field">
          <label class="label">Image URL</label>
          <div class="control">
            <input class="input is-large" type="url" placeholder="Image URL" required v-model="image_url">
          </div>
        </div>


        <div class="field">
          <label class="label">Breed</label>
          <div class="control">
            <div class="select">
              <select v-model="breed">
                <option value="Poodle">Poodle</option>
                <option value="Golden Retriever">Golden Retriever</option>
                <option value="Labrador Retriever">Labrador Retriever</option>
                <option value="Bulldog">Bulldog</option>
                <option value="Boxer">Boxer</option>
                <option value="Shih Tzu">Shih Tzu</option>
              </select>
            </div>
          </div>
        </div>

        <div class="field is-grouped is-grouped-right">
          <div class="control">
            <button class="button is-link" type="submit">Submit</button>
          </div>
        </div>
      </form>
    </div>
  </section>

  <section class="section container">
    <h1 class="title is-3">Dogs</h1>
    <progress class="progress is-large is-primary" max="100" v-if="dogs_loading">Loading</progress>
      <div class="columns is-multiline">
    <div class="column is-one-third" v-for="dog in dogs" :key="dog.name">
      <DogCard :name="dog.name" :image_url="dog.image_url" :breed="dog.breed" />
    </div>
  </div>
  </section>
</div>
</template>

<script>
  import {onMounted, ref} from 'vue'
  import DogCard from './components/DogCard.vue'

  export default {
    components: {
      DogCard
    },
    setup () {
      const dogs = ref();
      const name = ref();
      const image_url = ref();
      const breed = ref();
      const dogs_loading = ref();

      const getDogs = async () => {
        dogs_loading.value = true;
        const response = await fetch('http://localhost:8000/api/dog/');
        const json = await response.json();
        dogs.value = json;
        dogs_loading.value = false;
      }

      onMounted(async () => {
        getDogs();
      });

      const addDog = async () => {
        const response = await fetch('http://localhost:8000/api/dog', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            'name': name.value,
            'image_url': image_url.value,
            'breed': breed.value
          }),
        });
        if (response.ok) {
          getDogs();
          name.value = '';
          image_url.value = '';
          breed.value = '';
        } else {
          console.log('error');
        }
      }

      return {
        dogs, name, image_url, breed, getDogs, addDog, dogs_loading
      }
    }
  }
</script>

<style>
</style>