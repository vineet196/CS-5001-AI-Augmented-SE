import streamlit as st

def main():
    st.title("To-Do List")

    # Initialize session state for tasks if not already present
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Form for adding a new task
    with st.form("add_task_form"):
        task_input = st.text_input("Enter a new task:", key="task_input")
        submitted = st.form_submit_button("Add Task")

        if submitted and task_input.strip():
            st.session_state.tasks.append(task_input.strip())

    # Display current tasks
    if st.session_state.tasks:
        st.subheader("Your Tasks:")
        for i, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.write(f"- {task}")
            with col2:
                if st.button("Delete", key=f"del_{i}"):
                    st.session_state.tasks.pop(i)
                    st.rerun()  # Refresh the app to update the display
    else:
        st.info("No tasks yet. Add one above!")

if __name__ == "__main__":
    main()