# POC Core Model Extension

## Overview

This is a simple App for Nautobot. It is meant to be a proof of concept on how you can extend a core Nautobot model. It includes the following extensions to `dcim.Device`:

- Adding a field to the add and edit forms ([`override_views`](https://docs.nautobot.com/projects/core/en/stable/plugins/development/#replacing-views))
- Adding a field to the detail view ([`template_extensions`](https://docs.nautobot.com/projects/core/en/stable/plugins/development/#extending-object-detail-views))
- Adding a field to the table columns on the list view ([`override_views`](https://docs.nautobot.com/projects/core/en/stable/plugins/development/#replacing-views))
- Adding a field to allow it to be filtered on the list view ([`filter_extensions`](https://docs.nautobot.com/projects/core/en/stable/plugins/development/#extending-filters))
