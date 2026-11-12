I have MCP tools in this session. No shell commands were run; I only inspected the tool registry.

**Built in — orchestration and user input**

- `functions.exec`
- `functions.wait`
- `functions.request_user_input` — restricted to Plan mode
- `functions.request_user_input_async`

**Built in — available through `functions.exec`**

- `tools.apply_patch`
- `tools.exec_command`
- `tools.write_stdin`
- `tools.view_image`
- `tools.create_goal`
- `tools.get_goal`
- `tools.update_goal`
- `tools.list_mcp_resources`
- `tools.list_mcp_resource_templates`
- `tools.read_mcp_resource`
- `tools.clock__curr_time`
- `tools.image_gen__imagegen`
- `tools.web__run`

**Built in — clock**

- `clock.sleep`

**Built in — agent collaboration**

- `collaboration.spawn_agent`
- `collaboration.followup_task`
- `collaboration.send_message`
- `collaboration.interrupt_agent`
- `collaboration.list_agents`
- `collaboration.wait_agent`

**MCP server — `[plugin-server]`, provided by the `[bundled-plugin]` plugin**

- `mcp__[plugin-server].js`
- `mcp__[plugin-server].js_reset`

**Connector/app**

No dedicated connector/app tools are exposed.

**Skills**

Skills supply instructions and workflows, not additional callable tools. No separate skill tools are exposed.