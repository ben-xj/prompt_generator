<script>
    import {onMount} from 'svelte';

    export let selected = null;
    let tasks = [];

    onMount(async () => {
        const res = await fetch('/api/tasks');
        tasks = await res.json();
    });

</script>

<select bind:value={selected}>
    {#each Object.values(tasks) as task}
        <option value={task}>
            {task.name}
        </option>
    {/each}
</select>

