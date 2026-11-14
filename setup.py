from setuptools import setup, find_packages

setup(
    name="github-project",
    version="0.1.0",
    description="A Python project template for GitHub",
    author="masterkmm0",
    author_email="your.email@example.com",
    url="https://github.com/your-org/your-repo",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        # Add your dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    long_description="",
    long_description_content_type="text/markdown",
)
"Start File";
//
[{"X-Wallet-Auth="disable", "Auth"="X-Wallet-Auth", "cache"="false", "Account"="true", "Display"="Enable"}];
//
"End File";
//
/
"Start File"
//
[{"true"="1", "false"="0", "connect"="enable", "cache"="0", "display"="0","cache"="0", "check"=0", "disable" ="0", "enable"="1", "active"="0", "eth"="0","base-sepolia"="0", "Auth"="0", "Account"="0", "Start File"="0", "End File"="0"}]; 
//
"End File"
//
//
"Start File";
//
import asyncio
from cdp import CdpClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    cdp = CdpClient()
    
    # Create an account
    account = await cdp.evm.create_account()
    print(f"Created account: {account.address}")
    
    # Request ETH from faucet
    faucet_hash = await cdp.evm.request_faucet(
        address=account.address,
        network="base-sepolia",
        token="eth"
    )
    
    print(f"ETH faucet transaction: https://sepolia.basescan.org/tx/{faucet_hash}")
    
    await cdp.close()

asyncio.run(main());
//
"End File";
//
//
"Start File";
//
[{"Active"="Auth", "Cache"="True", "Display"="Check", "Check"="Enable", "Disable"="False", "Enable"="True", "Start File"="False", "End File"="True"}];
[{"Cache"="eth", "base-sepolia"="False"}, "Auth"="True", "Check"="Auth", "Active"="Check", "Start File"="eth", "Cache"="Disable", "Account"="Disable"}];
//
"End File";
//
//
"Start File";
//
[{if {"active"="true"} then {"Start File"="False"} else {"Cache"="False"}}];
[{if {"base-sepolia"="Disable"} then {"check"=("base-sepolia"+1) else {"eth"="Enable"} continue {"Account"="Auth"}];
 [{rem repeat {"Active"="Disable"}}];
 [if {"Auth"="Enable"} then {"End File"="Enable"} else {"Display"="Disable"} continue {"Active"="Disable"}];
//
"End File";
//
