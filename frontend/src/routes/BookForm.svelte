<script lang="ts">
	import { Button, Dropdown, TextInput, Spinner } from "nota-ui";
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

	onMount(async ()=>{
		let response = await fetch(`${env.PUBLIC_API_SERVER}/get_tags`, {
			method:"GET"
		})
		tags = JSON.parse(await response.text())
	})

	let selectedTags:string[] = []

	let ageRegex = /^[0-9]+$/i

	const submitData = async () => {
		postStatus = "loading"
		let user = {
			date:datePref,
			age:age,
			tags:selectedTags,
			length:bookLength
		}
		let response = await fetch(`${env.PUBLIC_API_SERVER}/get_recommendation`, {
			method:"POST",
			mode:"cors",
			headers:{
				"Content-Type":"application/json"
			},
			body:JSON.stringify(user)
		})
		if (response.status!=200){
			postStatus="error"
		} else {
			postStatus="complete"
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
	<div class="step">

		
	</div>
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
	<p>Finish</p>
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
</style>