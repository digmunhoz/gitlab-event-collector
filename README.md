# GitLab Events Collector

This software collects events from GitLab server, providing insights from users events. It consists of a data collector, an Elasticsearch instance, and a Grafana dashboard ready for data visualization.

As a technology leader, overseeing interactions with version control systems like Git is essential for various reasons. Firstly, it provides visibility into the progress of development tasks and projects. By tracking commits, branches, and merges, managers can understand the status of code changes and identify any bottlenecks or challenges the team may be facing.

Additionally, monitoring version control interactions can help with project management and resource allocation. Managers can track the distribution of work among team members, identify areas where additional support may be needed, and make informed decisions about project timelines and priorities.

Overall, by closely overseeing interactions with version control, technology managers can promote collaboration, ensure efficient project management, and make informed decisions to drive the success of development projects.

## Prerequisites
The only requirement to run this software is Docker.

## Setup

Before running the application, make sure to follow these steps:

1. Rename the `env_example` file to `env`.
2. Edit the `env` file and define the required environment variables.

### Variables from env file

|Variable|Default Value|Required|Definition|
|--------|-------------|--------|----------|
|GITLAB_API_URL|None|True|The gitlab API address|
|GITLAB_API_TOKEN|None|True|The gitlab API token|
|ELASTICSEARCH_ADDRESS|http://elasticsearch:9200|False|The elasticsearch address|
|ELASTICSEARCH_GITLAB_INDEX_PREFIX|gitlab_|False|The elasticsearch index prefix name|
|TIME_WINDOW_START_DATE|None|True|Begin date. Format: %Y-%m-%d|
|TIME_WINDOW_END_DATE|None|True|End date. Format: %Y-%m-%d|
|MAX_USERS|None|False|Max users to get from the Gitlab API|

## Execution

### Starting Elasticsearch and Grafana

Use the following command to start Elasticsearch and Grafana:

```bash
make start
```

This command will initialize the Elasticsearch database and Grafana server.

### Running the Collector
To execute the collector and start collecting events from GitLab repositories, use the following command:

```bash
make run
```

This command will launch the data collector and begin retrieving events from configured GitLab repositories.

## Dashboard Access

Once the Elasticsearch and Grafana services are up and running, you can access the Grafana dashboard by visiting http://localhost:3000 in your web browser. Use the default credentials (admin/password) to log in and explore the pre-configured dashboard called `Repository Events` for visualizing the collected data.

![Panel](/img/panel.png "Panel")

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.