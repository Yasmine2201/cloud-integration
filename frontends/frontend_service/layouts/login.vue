<script setup lang="ts">

</script>

<template>
  <div id="layoutLogin" class="grid grid-cols-2">
    <div class="use-bg-paper p-8 content-center">
      <div class="bg-white mt-5 p-3 shadow rounded">
        <slot/>
      </div>
    </div>
    <div class="use-bg-gradient flex">
      <div class="m-auto inline-block bg-white p-8 rounded-md">
        <p class="text-purple-400 text-xl">
          Words are the voice of the heart<br>
          Join us to <em class="text-purple-900">INTEGRATE</em> and <em class="text-purple-900">DEPLOY THEM</em>
        </p>
      </div>
    </div>
  </div>
</template>

<style>
html, body, #__nuxt, #__nuxt>div, #layoutLogin {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}
.use-bg-gradient {
  background-image: url("~/assets/background-gradient.png");
}
.use-bg-paper {
  background-image: url("~/assets/background-paper.png");
}
.use-bg-paper, .use-bg-gradient {
  background-size: cover;
  background-position: center;
}

</style>
