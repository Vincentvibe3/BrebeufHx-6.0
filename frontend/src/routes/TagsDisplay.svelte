<script lang="ts">
  import { Button } from "nota-ui";

	export let tags:string[]
	export let selectedTags:string[];

	const addTag = (value:string) =>{
		selectedTags.push(value)
		selectedTags=selectedTags
	}

	const removeTag = (value:string) =>{
		const index = selectedTags.indexOf(value);
		if (index > -1) { // only splice array when item is found
			selectedTags.splice(index, 1); // 2nd parameter means remove one item only
		}
		selectedTags=selectedTags
	}

</script>
<div class="container">
	{#each tags as tag}
		{#if selectedTags.includes(tag)}
			<Button style="margin:0.2rem;" type="secondary" on:click={()=>{removeTag(tag)}}>Remove {tag}</Button>
		{:else }
			<Button style="margin:0.2rem;" on:click={()=>{addTag(tag)}}>{tag}</Button>
		{/if}
	{/each }
</div>
<style>
	.container {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		align-items: center;
		justify-content: center;
	}
</style>