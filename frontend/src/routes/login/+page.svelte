<script>
	import { setTokens } from '$lib/stores/auth';
	import { goto } from '$app/navigation';
	const API = import.meta.env.VITE_API_BASE_URL;

	let tab = 'login';
	let username = '',
		password = '',
		email = '';
	$: canLogin = username.length >= 4 && password.length >= 8;
	$: canRegister = canLogin && /\S+@\S+\.\S+/.test(email);

	async function login() {
		if (!canLogin) return;
		const r = await fetch(`${API}/api/token/`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ username, password })
		});
		if (!r.ok) return alert('Login failed');
		setTokens(await r.json());
		goto('/');
	}

	async function register() {
		if (!canRegister) return;
		const r = await fetch(`${API}/api/register/`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ username, password, email })
		});
		if (!r.ok) return alert('Registration failed');
		await login();
	}
</script>

<main class="p-6 max-w-sm mx-auto">
	<div class="flex gap-4 mb-4">
		<button on:click={() => (tab = 'login')} class:active={tab === 'login'}>Login</button>
		<button on:click={() => (tab = 'register')} class:active={tab === 'register'}>Register</button>
	</div>

	<form on:submit|preventDefault={tab === 'login' ? login : register} class="flex flex-col gap-2">
		<input placeholder="Username" bind:value={username} />
		<input type="password" placeholder="Password" bind:value={password} />
		{#if tab === 'register'}
			<input type="email" placeholder="Email" bind:value={email} />
		{/if}
		<button type="submit">{tab === 'login' ? 'Login' : 'Register'}</button>
	</form>
</main>

<style>
	.active {
		border-bottom: 2px solid #8b3399;
		font-weight: 600;
	}
	input {
		padding: 0.6rem 0.8rem;
		border: 1px solid #ccc;
		border-radius: 0.4rem;
	}
	button {
		padding: 0.6rem 1rem;
		border-radius: 0.5rem;
		background: #8b3399;
		color: white;
	}
</style>
