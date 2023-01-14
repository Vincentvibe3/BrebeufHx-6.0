<script lang="ts">

  import { Header } from "nota-ui";
  import { onMount } from "svelte";
  import { env } from "$env/dynamic/public"
  import { each } from "svelte/internal";

	let books = [
			{id:1,
		"name":"",
		"age":1,
		"length":1,
		"yearPublished":1,
		"tags":[],
		"author":"",
		"image":"",
		"desc":""}
	]
	
  	onMount(async ()=>{
		let response = await fetch(`${env.PUBLIC_API_SERVER}/book/ALL`)
		books = await response.json()
		console.log(books)
	})

</script>
<Header
	img="https://images.unsplash.com/photo-1495446815901-a7297e633e8d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Ym9va3N8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60">
	Library
</Header>
<div class="recommendations">
	{#each books as book}
		<div class="book">
			<img src={book.image} alt="book image">
			<a href="/books/{book.id}">{book.name}</a>
			<p>{book.author}</p>
		</div>
	{/each}
</div>
<style>
	.recommendations {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		align-items: flex-start;
		justify-content: start;
	}

	.book {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		justify-content: center;
		background-color: var(--n300);
		padding: 1rem;
		border-radius: 0.2rem;
		width: fit-content;
		margin:1rem 1rem;
	}

	.book img {
		border-radius: 00.2rem;
	}

	.book a {
		text-decoration: none;
		font:var(--body);
		margin-top: 1rem;
	}

	.book a + .book p {
		margin-top: 1rem;
	}
</style>