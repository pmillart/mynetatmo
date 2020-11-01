SELECT 
    --json_value(jsonContent, '$.user.mail') as mail,
    json_value(jsoncontent, '$.devices[0]._id') as id,
    json_value(jsoncontent, '$.devices[1]._id') as id2,
    DATEADD(SS, CONVERT(BIGINT, json_value(jsoncontent, '$.devices[1].dashboard_data.time_utc')), '19700101') as Time_UTC,
    json_value(jsoncontent, '$.devices[0].dashboard_data.Temperature') as temperature,
    json_value(jsoncontent, '$.devices[0].modules[0].dashboard_data.Temperature') as outside,
    json_value(jsoncontent, '$.devices[0].dashboard_data.Humidity') as Humidity,
    json_value(jsoncontent, '$.devices[0].dashboard_data.Pressure') as Pressure,
    json_value(jsoncontent, '$.devices[0].dashboard_data.temp_trend') as trend,
    jsonContent
FROM
    OPENROWSET(
        BULK 'https://wesynapseadls.dfs.core.windows.net/wesynapsefs/netatmo/*.json',
        FORMAT='CSV',
        FIELDTERMINATOR ='0x0b',
        FIELDQUOTE = '0x0b',
        ROWTERMINATOR = '0x0b'
    )
    WITH (
        jsonContent varchar(8000)
    ) AS [r]
order by Time_UTC desc
--WHERE
--    JSON_VALUE(jsonContent, '$.title') = 'Probabilistic and Statistical Methods in Cryptology, An Introduction by Selected Topics';

