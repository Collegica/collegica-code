No shell commands were run. The callable tools are listed below; names under `tools.*` are accessed through `functions.exec`.

**Built in — orchestration and user input**

- `functions.exec`
- `functions.wait`
- `functions.request_user_input` — restricted to Plan mode
- `functions.request_user_input_async`

**Built in — execution, files, and goals**

- `tools.apply_patch`
- `tools.exec_command`
- `tools.write_stdin`
- `tools.view_image`
- `tools.create_goal`
- `tools.get_goal`
- `tools.update_goal`

**Built in — web, images, and time**

- `tools.web__run`
- `tools.image_gen__imagegen`
- `tools.clock__curr_time`
- `clock.sleep`

**Built in — agent collaboration**

- `collaboration.spawn_agent`
- `collaboration.followup_task`
- `collaboration.interrupt_agent`
- `collaboration.list_agents`
- `collaboration.send_message`
- `collaboration.wait_agent`

**Built in — MCP resource access**

- `tools.list_mcp_resources`
- `tools.list_mcp_resource_templates`
- `tools.read_mcp_resource`

**MCP server / plugin — `[bundled-plugin]`**

- `mcp__[plugin-server].js`
- `mcp__[plugin-server].js_reset`

I **do have MCP tools**: the two computer-use tools above.

**Connector/app**

No separate connector/app tools are exposed in this session.

**Skills**

Skills supply instructions and workflows, not additional callable tools. No skill-specific tools are exposed.