No shell commands were run. **No MCP server tools, plugin tools, or connector/app tools are exposed in this session.**

**Built-in tools — directly callable**

- `functions.exec`
- `functions.wait`
- `functions.request_user_input`
- `functions.request_user_input_async`
- `clock.sleep`
- `collaboration.followup_task`
- `collaboration.interrupt_agent`
- `collaboration.list_agents`
- `collaboration.send_message`
- `collaboration.spawn_agent`
- `collaboration.wait_agent`

`functions.request_user_input` is restricted to Plan mode; this session is in Default mode.

**Built-in tools — callable through `functions.exec`, using these exact names**

- `tools.apply_patch`
- `tools.exec_command`
- `tools.write_stdin`
- `tools.view_image`
- `tools.create_goal`
- `tools.get_goal`
- `tools.update_goal`
- `tools.clock__curr_time`
- `tools.image_gen__imagegen`
- `tools.web__run`
- `tools.list_mcp_resources`
- `tools.list_mcp_resource_templates`
- `tools.read_mcp_resource`

The three MCP resource utilities are built-in interfaces; their presence does not mean any MCP server tools are connected.

**Skills**

Skills provide instructions, not additional callable tools. No skill-specific tools are exposed. Installed skills may describe CLI workflows, but those CLIs are not separate tools in this session.