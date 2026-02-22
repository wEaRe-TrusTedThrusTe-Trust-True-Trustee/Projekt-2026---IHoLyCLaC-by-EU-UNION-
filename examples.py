"""
Example usage scenarios for EU-UNION Patent Expert System
Demonstrates various features of the Experten Modus (Expert Mode)
"""

from patent_system import (
    PatentExpertSystem,
    PatentOffice,
    JurisdictionType,
    PatentStatus
)


def example_single_jurisdiction():
    """Example: Patent application for single jurisdiction"""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Single Jurisdiction Patent (EU-UNION)")
    print("=" * 70)
    
    system = PatentExpertSystem()
    
    app = system.create_application(
        title="Advanced Data Processing Algorithm",
        inventor="Maria Schmidt",
        description="Novel algorithm for efficient data processing in distributed systems",
        jurisdictions=[JurisdictionType.EU_UNION],
        patent_offices=[PatentOffice.EUIPO]
    )
    
    print(f"\nApplication Created: {app.application_id}")
    print(f"Status: {app.status.value}")
    print(f"Jurisdictions: {[j.value for j in app.jurisdictions]}")
    print(f"Patent Offices: {[o.value for o in app.patent_offices]}")


def example_multi_jurisdiction():
    """Example: Patent application for multiple jurisdictions"""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Multi-Jurisdiction Patent (EU, USA, Australia)")
    print("=" * 70)
    
    system = PatentExpertSystem()
    
    app = system.create_application(
        title="Renewable Energy Storage System",
        inventor="John Anderson",
        description="Innovative battery technology for renewable energy storage",
        jurisdictions=[
            JurisdictionType.EU_UNION,
            JurisdictionType.USA,
            JurisdictionType.AUSTRALIA
        ],
        patent_offices=[
            PatentOffice.EUIPO,
            PatentOffice.EPA,
            PatentOffice.WIPO
        ]
    )
    
    print(f"\nApplication Created: {app.application_id}")
    print(f"Status: {app.status.value}")
    print(f"Trademark: {app.trademark}")
    print("\nCoverage:")
    for jurisdiction in app.jurisdictions:
        print(f"  ✓ {jurisdiction.value}")


def example_all_partners():
    """Example: Patent application for all partner jurisdictions"""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Full Partner Network Coverage")
    print("=" * 70)
    
    system = PatentExpertSystem()
    
    app = system.create_application(
        title="Global Communication Protocol",
        inventor="Dr. Elena Rossi",
        description="Universal communication protocol for international systems",
        jurisdictions=[
            JurisdictionType.EU_UNION,
            JurisdictionType.AUSTRALIA,
            JurisdictionType.USA,
            JurisdictionType.SPAIN,
            JurisdictionType.SWITZERLAND,
            JurisdictionType.ITALY,
            JurisdictionType.PORTUGAL,
            JurisdictionType.VATICAN_CITY
        ],
        patent_offices=[
            PatentOffice.EUIPO,
            PatentOffice.EPA,
            PatentOffice.WIPO
        ]
    )
    
    print(f"\nApplication Created: {app.application_id}")
    print(f"Status: {app.status.value}")
    print(f"Registration Location: {app.registration_location}")
    print(f"\nFull International Coverage: {len(app.jurisdictions)} jurisdictions")
    print(f"Patent Offices: {len(app.patent_offices)} offices")


def example_multiple_applications():
    """Example: Managing multiple patent applications"""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Multiple Patent Applications Management")
    print("=" * 70)
    
    system = PatentExpertSystem()
    
    # Create multiple applications
    applications = [
        system.create_application(
            title="AI-Powered Medical Diagnosis System",
            inventor="Dr. Thomas Mueller",
            description="Machine learning system for medical diagnosis",
            jurisdictions=[JurisdictionType.EU_UNION, JurisdictionType.USA],
            patent_offices=[PatentOffice.EUIPO, PatentOffice.WIPO]
        ),
        system.create_application(
            title="Quantum Computing Framework",
            inventor="Prof. Sophie Laurent",
            description="Framework for quantum computing applications",
            jurisdictions=[JurisdictionType.EU_UNION, JurisdictionType.SWITZERLAND],
            patent_offices=[PatentOffice.EPA, PatentOffice.WIPO]
        ),
        system.create_application(
            title="Blockchain Security Protocol",
            inventor="Carlos Martinez",
            description="Enhanced security protocol for blockchain networks",
            jurisdictions=[JurisdictionType.SPAIN, JurisdictionType.PORTUGAL],
            patent_offices=[PatentOffice.EUIPO]
        )
    ]
    
    print(f"\nTotal applications created: {len(applications)}")
    print("\nApplications Summary:")
    for app in applications:
        print(f"\n  • {app.title}")
        print(f"    ID: {app.application_id}")
        print(f"    Status: {app.status.value}")
        print(f"    Inventor: {app.inventor}")


def example_application_filtering():
    """Example: Filtering and querying applications"""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Application Filtering and Queries")
    print("=" * 70)
    
    system = PatentExpertSystem()
    
    # Create various applications
    system.create_application(
        title="Solar Panel Technology",
        inventor="Anna Petrov",
        description="Advanced solar panel efficiency technology",
        jurisdictions=[JurisdictionType.EU_UNION],
        patent_offices=[PatentOffice.EUIPO]
    )
    
    system.create_application(
        title="Water Purification System",
        inventor="Michael Chen",
        description="Novel water purification for developing regions",
        jurisdictions=[JurisdictionType.AUSTRALIA, JurisdictionType.USA],
        patent_offices=[PatentOffice.WIPO]
    )
    
    system.create_application(
        title="Sustainable Agriculture Method",
        inventor="Isabella Romano",
        description="Sustainable farming technique for arid climates",
        jurisdictions=[JurisdictionType.ITALY, JurisdictionType.SPAIN],
        patent_offices=[PatentOffice.EUIPO]
    )
    
    # Query applications
    print(f"\n📊 Total applications: {len(system.list_applications())}")
    
    registered = system.get_applications_by_status(PatentStatus.REGISTERED)
    print(f"✅ Registered patents: {len(registered)}")
    
    eu_patents = system.get_applications_by_jurisdiction(JurisdictionType.EU_UNION)
    print(f"🇪🇺 EU-UNION patents: {len(eu_patents)}")
    
    italy_patents = system.get_applications_by_jurisdiction(JurisdictionType.ITALY)
    print(f"🇮🇹 Italy patents: {len(italy_patents)}")
    
    australia_patents = system.get_applications_by_jurisdiction(JurisdictionType.AUSTRALIA)
    print(f"🇦🇺 Australia patents: {len(australia_patents)}")


def example_export_summary():
    """Example: Exporting patent summaries"""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Export Patent Application Summary")
    print("=" * 70)
    
    system = PatentExpertSystem()
    
    app = system.create_application(
        title="Advanced Cryptography System",
        inventor="Dr. Klaus Wagner",
        description="Post-quantum cryptography for secure communications",
        jurisdictions=[
            JurisdictionType.EU_UNION,
            JurisdictionType.SWITZERLAND,
            JurisdictionType.USA
        ],
        patent_offices=[
            PatentOffice.EUIPO,
            PatentOffice.EPA,
            PatentOffice.WIPO
        ]
    )
    
    summary = system.export_application_summary(app.application_id)
    print(summary)


def main():
    """Run all examples"""
    print("\n" + "=" * 70)
    print("EU-UNION PATENT EXPERT SYSTEM - USAGE EXAMPLES")
    print("Projekt-2026 - IHoLyCLaC by EU-UNION")
    print("Experten Modus (Expert Mode) - Patent Automatic")
    print("=" * 70)
    
    # Run all example scenarios
    example_single_jurisdiction()
    example_multi_jurisdiction()
    example_all_partners()
    example_multiple_applications()
    example_application_filtering()
    example_export_summary()
    
    print("\n" + "=" * 70)
    print("ALL EXAMPLES COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("\n✅ Expert Mode: Automatic Processing Enabled")
    print("✅ Trademark: Hnoss - by Government")
    print("✅ Registration: Detmold, 22.2.2026 - 06:28 TimeCLock+")
    print()


if __name__ == "__main__":
    main()
