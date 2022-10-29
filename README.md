# Fields Renamer

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Fields Renamer                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/fields-renamer](https://hub.docker.com/r/weevenetwork/fields-renamer) |
| Authors        | Jakub Grzelak                    |

- [Fields Renamer](#fields-renamer)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Rename fields (labels) in your data. List of comma (,) separated pairs of fields to rename in format old_name=new_name. For example, to rename fields `temp` to `temperature` and `V` to `volume` the list should look like `temp=temperature, V=volume`.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Rename Fields    | RENAME_FIELDS         | string   | List of comma (,) separated pairs of fields to rename in format old_name=new_name.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| EGRESS_URLS            | string | HTTP ReST endpoints for the next module         |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "temp": 12,
    "V": 3
}
```

* array of JSON body objects, example:

```json
[
    {
        "temp": 12,
        "V": 3
    },
    {
        "temp": 21,
        "V": 4
    }
]
```

## Output

If Rename Fields is set to `temp=temperature, V=volume` Output of this module is:

* JSON body single object, example:

```json
{
    "temperature": 12,
    "volume": 3
}
```

* array of JSON body objects, example:

```json
[
    {
        "temperature": 12,
        "volume": 3
    },
    {
        "temperature": 21,
        "volume": 4
    }
]
```
