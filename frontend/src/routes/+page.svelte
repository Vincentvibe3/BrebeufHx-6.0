<script lang="ts">
	import {Header} from "nota-ui"
  	import BookForm from "./BookForm.svelte";

	export let sidebarOpen=false;
</script>
<Header
	img="https://images.unsplash.com/photo-1495446815901-a7297e633e8d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Ym9va3N8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60">
	Book Finder
</Header>
<main>
	<BookForm></BookForm>
</main>
<style>
	main {
		margin: 2rem 2rem;
	}


</style>