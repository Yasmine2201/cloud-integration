<script setup lang="ts">
import {useAuthStore} from '~/store/auth';

const router = useRouter();

const {logoutUser} = useAuthStore();
const {isAuthenticated} = useAuthStore();


console.log(isAuthenticated);

const navLinks = computed(() => {
  if (isAuthenticated ) {
    return [
      {label: "Home", icon: "i-heroicons-home", to: "/home"},
      {label: "Profile", icon: "i-heroicons-user", to: "/profile"},
      {label: "Logout", icon: "i-heroicons-arrow-left-on-rectangle", click: logout}
    ];
  } else {
    return [
      {label: "Login", icon: "i-heroicons-arrow-right-on-rectangle", to: "/login"},
      {label: "Register", icon: "i-heroicons-user-plus", to: "/register"}
    ];
  }
});

async function logout() {
  await logoutUser();
};
</script>

<template>
  <div class="main-container gap-10">
    <UHorizontalNavigation :links="navLinks" class="shadow p-2"/>

    <div id="content" class="main-container d-flex flex-column align-items-center">
      <slot/>
    </div>
  </div>
</template>


<style>

</style>