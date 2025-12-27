# List of machines with credentials
$machines = @(
    @{ip = "192.168.31.88"; user = "eims"; password = "Pineappleismyfavouritefruit730'"}
)

# Function to check if a host is reachable
function Test-HostReachability {
    param (
        [string]$ip
    )
    $pingResult = Test-Connection -ComputerName $ip -Count 1 -Quiet
    return $pingResult
}

# Function to collect PC health info
function Get-PCHealth {
    param (
        [string]$ip,
        [string]$user,
        [string]$password
    )

    if (-not (Test-HostReachability -ip $ip)) {
        return [PSCustomObject]@{
            IP = $ip
            ComputerName = $null
            Error = "Host unreachable"
        }
    }

    # Creating credentials for remote access
    $securePassword = ConvertTo-SecureString $password -AsPlainText -Force
    $credentials = New-Object System.Management.Automation.PSCredential ($user, $securePassword)

    try {
        # Get system information via WMI
        $sysInfo = Get-WmiObject -Class Win32_ComputerSystem -ComputerName $ip -Credential $credentials
        $osInfo = Get-WmiObject -Class Win32_OperatingSystem -ComputerName $ip -Credential $credentials
        $cpuInfo = Get-WmiObject -Class Win32_Processor -ComputerName $ip -Credential $credentials
        $diskInfo = Get-WmiObject -Class Win32_LogicalDisk -ComputerName $ip -Filter "DriveType=3" -Credential $credentials

        # Format disk info
        $diskInfoFormatted = $diskInfo | ForEach-Object {
            "$($_.DeviceID): $( [math]::Round($_.FreeSpace / 1e9, 2)) GB free of $( [math]::Round($_.Size / 1e9, 2)) GB"
        } -join "; "

        # Collect health info
        return [PSCustomObject]@{
            IP = $ip
            ComputerName = $sysInfo.Name
            Manufacturer = $sysInfo.Manufacturer
            Model = $sysInfo.Model
            OS = $osInfo.Caption
            OSVersion = $osInfo.Version
            Uptime_Days = [math]::Round((New-TimeSpan -Start $osInfo.LastBootUpTime).Days, 2)
            TotalMemoryGB = [math]::Round($sysInfo.TotalPhysicalMemory / 1e9, 2)
            FreeMemoryGB = [math]::Round($osInfo.FreePhysicalMemory / 1e6, 2)
            CPUName = $cpuInfo.Name
            CPULoad = $cpuInfo.LoadPercentage
            DiskInfo = $diskInfoFormatted
            Error = $null
        }
    } catch {
        return [PSCustomObject]@{
            IP = $ip
            ComputerName = $null
            Error = $_.Exception.Message
        }
    }
}

# Collect data from all machines
$allResults = @()
foreach ($machine in $machines) {
    Write-Host "Checking $($machine.ip) ..."
    $result = Get-PCHealth -ip $machine.ip -user $machine.user -password $machine.password
    $allResults += $result
}

# Export results to Excel (requires ImportExcel module)
$allResults | Export-Excel -Path "pc_health.xlsx" -WorksheetName "PC Health Report" -AutoSize -AutoFilter
Write-Host "`n✅ PC health report saved to pc_health.xlsx"