# Evidence: Quality at Desk — Boilerplate Code Reduction with Lombok (HSDP)

## Source
- **File:** `20200408_QualityAtDesk_BoilerCodeReduction_Lombok_HSDP.PNG`
- **Date:** 2020-04-08
- **Ingested:** 2026-08-06
- **Channel:** Philips Internal (Yammer - Software Center of Excellence SW_CoE)
- **Category:** Informal Feedback

## Metadata
- **From:** Gaidhani, Suyog
- **To/About:** Vellal, Dattatreya (and SW CoE team including Hu, Aravind)
- **Context:** Suyog Gaidhani shared how a discussion with the SW CoE Team (including Datta) about Lombok inspired his HSDP Insights team to adopt the library, reducing nearly 24% of duplication in key modules. This was posted as a "Quality at Desk" success story on Yammer, seen by 204 people.
- **Platform:** Yammer (Software Center of Excellence group)
- **Reactions:** Hristov, Zoran; Silveira, Matheus Soares; Jagadeesan, Sundaresan; and 8 others reacted

## Datta's Involvement
- **Role at time:** Senior Software Engineer / SW CoE
- **Involvement type:** Direct influence — credited for advocating Lombok adoption

## Key Quotes
> "During a discussion with the SW CoE Team a couple of weeks back, Vellal, Dattatreya and Hu, Aravind talked about a small Java library called as Lombok and extolled its virtues in reducing the boilerplate code that inevitably makes its way into any code base."

> "I was suitably impressed and went back to my team to check why we shouldn't be using such a simple technique in our HSDP Insights services."

> "Given that we have a fair number of DTO and Entity classes, using Lombok helped us to reduce nearly 24% of duplication in one of our key modules."

## Full Content
```
Software Center of Excellence (SW_CoE)

Gaidhani, Suyog — April 8 at 10:38 AM — Edited

During a discussion with the SW CoE Team a couple of weeks back, Vellal, Dattatreya and Hu, Aravind talked about a small Java library called as Lombok and extolled its virtues in reducing the boilerplate code that inevitably makes its way into any code base. The way in which Lombok works is via annotations that can be added to the Java class for which common methods are desired. These annotations are self-descriptive in their names and a few examples of these are @Getter, @Setter, @ToString and so on. Using these annotations, reduces duplication and also saves on the developer efforts.

I was suitably impressed and went back to my team to check why we shouldn't be using such a simple technique in our HSDP Insights services. The team was happy to report that they had already been doing so since last year when the team took this up to rein in our duplicate code KPI. Given that we have a fair number of DTO and Entity classes, using Lombok helped us to reduce nearly 24% of duplication in one of our key modules. Since then the team has been a regular user of the library including using it in our recently released HSDP De-Identification service.

Here is a simple code snippet on how code with and without Lombok looks and the difference is apparent:

/*Code without Lombok*/
public class AssociatedDTO implements Serializable {
    private String scriptType;
    private String scriptName;

    public String getScriptType() {
        return scriptType;
    }

    public void setScriptType(String scriptType) {
        this.scriptType = scriptType;
    }

    public String getScriptName() {
        return scriptName;
    }

    public void setScriptName(String scriptName) {
        this.scriptName = scriptName;
    }
}

/*Code with Lombok*/
@Getter
@Setter
public class AssociatedDTO implements Serializable {
    private String scriptType;
    private String scriptName;
}

In case, anyone would like to know more about using this in their code base, please feel free to reach out to P, Rohith Kumar, Elapanda, Ramakrishna and Agrawal, Praveen.

Thank you for the session Jagadeesan, Sundaresan!

cc: Vellal, Dattatreya, Supakar, Sitangshu, Elapanda, Ramakrishna, Hu, Aravind, P, Rohith Kumar, Agrawal, Praveen, and Jagadeesan, Sundaresan

Hristov, Zoran, Silveira, Matheus Soares, Jagadeesan, Sundaresan, and 8 others reacted to this
Seen by 204
```
