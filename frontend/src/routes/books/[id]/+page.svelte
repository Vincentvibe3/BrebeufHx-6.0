<script>
	import {page} from "$app/stores"
	import { Header, Button } from "nota-ui";
  import { onMount } from "svelte";
  import { env } from "$env/dynamic/public"

	let id = $page.params.id
	let book={id:1,
	"name":"",
	"age":1,
	"length":1,
	"yearPublished":1,
	"tags":[],
	"author":"",
	"image":"",
	"desc":""};

	onMount(async ()=>{
		let response = await fetch(`${env.PUBLIC_API_SERVER}/book/${id}`)
		book = await response.json()
		console.log(book)
	})

</script>
<Header
	img={book.image}>
	{book.name}
</Header>
<main>
	<h2>A book by {book.author}</h2>
	<h3>Publishing Date</h3>
	<p>{book.yearPublished}</p>
	<h3>Description</h3>
	<p>{book.desc}</p>
	<h3>Tags</h3>
	<div class="container">
		{#each book.tags as tag}
			<Button style="margin:0.2rem;" disabled>{tag}</Button>
		{/each }
	</div>
</main>
<style>
	main {
		padding: 1rem 2rem;
	}

	h3 {
		font: var(--subtitle);
	}
	h2 {
		font:var(--heading5)
	}
	.container {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		align-items: center;
		justify-content: start;
	}
	.container:global( svg ) {
		fill: var(--btnSecondaryIcon);
		stroke: var(--btnSecondaryIcon);
	}
</style>