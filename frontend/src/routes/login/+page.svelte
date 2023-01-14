<script lang="ts">
	import { Button, PasswordInput, TextInput  } from "nota-ui";
	let username = "";

</script>
<main>
	<div class="wrapper">
		<h1>Login</h1>
		<p>Username</p>
		<TextInput style="width:100%;" bind:text={username} placeholder="Username"></TextInput>
		<p>Password</p>
		<PasswordInput style="width:100%;" text="" placeholder="Password"></PasswordInput>
		<div class="actionBar">
			<Button style="height:3rem;">Login</Button>
		</div>
	</div>
</main>
<style>
	.wrapper {
		width: 25%;
		padding: 5rem;
		background-color: var(--n200);
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		justify-content: center;
	}

	main {
		width: 100vw;
		height: 100vh;
		color: var(--n200);
		background-image: url("https://images.unsplash.com/photo-1673271044466-b23ea152130f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80");
		background-size: cover;
		display: flex;
		overflow: hidden;
	}

	p {
		color: var(--n800);
		font:var(--body);
		margin: 1rem 0rem;
	}

	h1 {
		color: var(--n800);
		font: var(--heading1);
	}

	.actionBar {
		margin-top:2rem ;
	}
</style>