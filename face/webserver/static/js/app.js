
 function manage_buttons_in_cards(task)
{
   if (document.getElementById(task + "-stop-button"))
   {
         task_running = document.getElementById("task-status-"+task).value
         console.log("manage buttons "+ task + " " + task_running)
        if (task_running == 1)
        {
            console.log("task is running")
            document.getElementById(task + "-start-button").classList.add("d-none")
            document.getElementById(task + "-stop-button").classList.remove("d-none")
        }
        else
        {
            console.log("task is stopped")
            document.getElementById(task + "-start-button").classList.remove("d-none")
            document.getElementById(task + "-stop-button").classList.add("d-none")
        }
   }

}
    function toggle_read_task_in_cards(task)
    {
             console.log(task)
             toggle_task_state(task)
             if(document.getElementById("task-status-"+task).value==1)
                document.getElementById("task-status-"+task).value = 0
             else
                document.getElementById("task-status-"+task).value = 1
                console.log(document.getElementById("task-status-"+task).value)
             manage_buttons_in_cards( task)
    }

