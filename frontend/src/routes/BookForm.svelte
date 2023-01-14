<script lang="ts">
	import { Button, Dropdown, TextInput, Spinner, Separator } from "nota-ui";
  import TagsDisplay from "./TagsDisplay.svelte";
  import { env } from "$env/dynamic/public"
  import { onMount } from "svelte";

	let age = "";
	let ageValid:boolean;
	let bookValid:boolean;
	let bookLength=""
	let datePref=""
	let postStatus=""
	let datePrefOptions:string[] = ['contemporary', 'modern', 'renaissance', 'gothic', 'baroque', 'middle ages', 'antiquity']
	let bookLengthOptions:string[] = ["short", "medium", "long"]
	let tags:string[] = []

	let recs = [{id:1,
		"name":"",
		"age":1,
		"length":1,
		"yearPublished":1,
		"tags":[],
		"author":"",
		"image":"",
		"desc":""}]

	onMount(async ()=>{
		let response = await fetch(`${env.PUBLIC_API_SERVER}/get_tags`, {
			method:"GET"
		})
		tags = JSON.parse(await response.text())
		recs = []
	})

	let selectedTags:string[] = []

	let ageRegex = /^[0-9]+$/i

	const submitData = async () => {
		postStatus = "loading"
		let user = {
			date:datePref,
			age:parseInt(age),
			tags:selectedTags,
			length:parseInt(bookLength)
		}
		let response = await fetch(`${env.PUBLIC_API_SERVER}/get_recommendation`, {
			method:"POST",
			mode:"cors",
			headers:{
				"Content-Type":"application/json"
			},
			body:JSON.stringify(user)
		})
		console.log(response.status)
		if (response.status!=200){
			postStatus="error"
		} else {
			postStatus="complete"
			recs = await response.json()
		}
	}

	const verifyAge = () => {
		let matchResult = age.match(ageRegex)
		ageValid = matchResult!=null
	}

	const verifyBookLength = () => {
		let matchResult = bookLength.match(ageRegex)
		bookValid = matchResult!=null
	}


</script>
<div class="container">
	<h2>Find books here</h2>
	{#if recs.length != 0}
		<Button on:click={()=>{recs=[]}}>Restart</Button>
		<p>Recommended Books</p>
		<div class="recommendations">
			{#each recs as book}
				<div class="book">
					<img src={book.image} alt="book image">
					<a href="/books/{book.id}">{book.name}</a>
					<p>{book.author}</p>
				</div>
			{/each}
		</div>
	{:else}
		<p>How old are you?</p>
		<TextInput bind:text={age} on:input={verifyAge} bind:valid={ageValid} placeholder="Age"></TextInput>
		<p>How long do you like your books?</p>
		<Dropdown bind:optionText={bookLength}>
			<option value="0">Select an option:</option>
			{#each bookLengthOptions as option}
				<option value={option}>{option}</option>
			{/each}	
		</Dropdown>
		<p>What era of books do you prefer?</p>
		<Dropdown bind:optionText={datePref} bind:options={datePrefOptions} >
			<option value="0">Select an option:</option>
			{#each datePrefOptions as option}
				<option value={option}>{option}</option>
			{/each}	
		</Dropdown>
		<p>What kind of books do you like?</p>
		<TagsDisplay bind:tags={tags} bind:selectedTags={selectedTags} ></TagsDisplay>
		<p>Show Me Books</p>
		<Button 
			on:click={submitData}>
			Submit
		</Button>
		{#if postStatus!="none"}
			<div class="statusWrapper">
				<Spinner bind:status={postStatus}></Spinner>
				{#if postStatus=="error"}
					<p>Something went wrong</p>
				{:else if postStatus=="complete"}
					<p>Done</p>
				{/if}
			</div>
		{/if}
	{/if}
</div>
<style>
	.statusWrapper {
		display: flex;
		flex-direction: row;
		align-items: center;
		width: fit-content;
		margin: 1rem 0rem;
	}

	.statusWrapper p {
		margin: 0px;
		margin-left: 1rem;
	}

	.recommendations {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		align-items: center;
		justify-content: space-between;
	}

	/* .book {
		background-color: var(--n300);
		padding: 1rem;
		border-radius: 0.2rem;
		width: fit-content;
		margin:0rem 1rem;
	} */

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
		width: 100%;
		height: 8rem;
		object-fit: cover;
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