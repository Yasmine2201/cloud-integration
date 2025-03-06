<script setup lang="ts">
import {useAuthStore} from '~/store/auth';

const router = useRouter();
const {logoutUser} = useAuthStore();
const {isAuthenticated} = useAuthStore();


const navLinks = computed(() => {
  if (isAuthenticated ) {
    return [
      {label: "Home", icon: "i-heroicons-home", to: "/home"},
      {label: "Profile", icon: "i-heroicons-user", to: "/profile"},
      {label: "Logout", icon: "i-heroicons-arrow-left-on-rectangle", click: logout}
    ];
  } else {
    return [
      {label: "Login", icon: "i-heroicons-arrow-right-on-rectangle", to: "/auth/login"},
      {label: "Register", icon: "i-heroicons-user-plus", to: "/auth/register"}
    ];
  }
});

async function logout() {
  await logoutUser();
};
</script>

<template>
  <div id="layoutDefault" class="flex flex-col">
    <UHorizontalNavigation :links="navLinks" class="shadow p-2"/>

    <div id="content" class="main-container d-flex flex-column align-items-center use-bg-feed flex-grow">
      <slot/>
    </div>
  </div>
</template>


<style>

html, body, #__nuxt, #__nuxt>div, #layoutDefault {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}

.use-bg-feed {
  background-image: url("~/assets/background-feed.svg");
}
.use-bg-feed {
  background-size: cover;
  background-position: center;
}
</style>