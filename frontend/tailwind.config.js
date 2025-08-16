/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    './src/**/*.{html,js,svelte,ts}',
    './node_modules/@skeletonlabs/skeleton-svelte/dist/**/*.{svelte,js}'
  ],
  theme: {
    extend: {}
  },
  plugins: []
};
