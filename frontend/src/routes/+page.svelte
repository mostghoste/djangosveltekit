<script>
	import { user } from '$lib/stores/auth';
	import { goto } from '$app/navigation';
	$: loggedIn = !!$user;
</script>

<main class="p-6 max-w-xl mx-auto">
	<h1 class="text-2xl font-bold mb-3">Django + SvelteKit</h1>
	<p class="mb-6">Barebones starter with JWT auth; plug your features here.</p>

	{#if loggedIn}
		<button class="btn" on:click={() => goto('/profile')}>Go to profile</button>
	{:else}
		<button class="btn" on:click={() => goto('/login')}>Login / Register</button>
	{/if}
</main>

<style>
	.btn {
		padding: 0.6rem 1rem;
		border-radius: 0.5rem;
		background: #8b3399;
		color: white;
	}
</style>
